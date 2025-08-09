export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Only POST allowed", { status: 405 });
    }

    try {
      const data = await request.json();

      // create jobId
      const jobId = crypto.randomUUID();

      // for saving in firestore database
      const jobData = {
        id: jobId,
        status: "processing",
        payload: data,
        created_at: new Date().toISOString(),
      };

      
      const firestoreUrl = `https://firestore.googleapis.com/v1/projects/"YOUR_FIREBASE_Project_id"/databases/(default)/documents/jobs?key="FIRE_BASE_API_KEY"`;

      const firestoreRes = await fetch(firestoreUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          fields: {
            id: { stringValue: jobData.id },
            status: { stringValue: jobData.status },
            payload: { stringValue: JSON.stringify(jobData.payload) },
            created_at: { stringValue: jobData.created_at },
          },
        }),
      });

      if (!firestoreRes.ok) {
        throw new Error("Failed to save job in Firestore");
      }

      // for Fastapi process
      const fastApiRes = await fetch("NGROK URL/Process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(jobData),
      });

      if (!fastApiRes.ok) {
        throw new Error("Failed to send job to FastAPI");
      }

      // response to client
      return new Response(
        JSON.stringify({ jobId, message: "Job created successfully" }),
        { status: 202, headers: { "Content-Type": "application/json" } }
      );
    } catch (err) {
      return new Response(
        JSON.stringify({ error: err.message }),
        { status: 500, headers: { "Content-Type": "application/json" } }
      );
    }
  },
};
