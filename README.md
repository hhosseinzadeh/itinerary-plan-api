# Travel Itinerary API

A FastAPI-based service that generates detailed travel itineraries using OpenAI's GPT-4o-mini model, stores results in Firebase Firestore, and leverages Cloudflare Workers for scalable, secure, and serverless request processing.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Introduction

This API accepts travel job requests with destination and duration details, then uses OpenAI's GPT-4o-mini to generate a day-by-day travel itinerary. The generated itinerary is stored and managed in Firebase Firestore for easy retrieval.

To ensure high availability, low latency, and enhanced security, Cloudflare Workers are integrated as a serverless edge layer that processes incoming requests, manages API routing, and handles authentication seamlessly.

The goal is to provide an automated, AI-powered backend for travel planning applications with a scalable, globally distributed infrastructure.


The workflow of the request from the user side, along with the data flow, processing, and storage, is as follows:


[User] → POST → [Cloudflare Worker] 
                        ↳ creates jobId + Firestore doc (status: processing)
                        ↳ POST to Ngrok/FastAPI server → LLM call
                                                         ↳ update Firestore (status: completed)
---

## Features

- Generate multi-day travel itineraries with themed daily activities  
- Store job status and results in Firebase Firestore  
- Async processing with FastAPI for efficient backend handling  
- Cloudflare Workers for serverless, edge-based request processing and security  
- REST API endpoint designed for easy integration with web and mobile apps  
- Ngrok support for local tunneling during development  

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/travel-itinerary-api.git
   cd travel-itinerary-api

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. To work with Cloudflare from your local system without the need for Node.js and npm installed, then need to install wrangler by running the following commands:
  
   ```bash
   npm install -g wrangler
 
4. then write thess commands in your system terminal:
   ```bash
   wrangler login
   wrangler generate itinerary-worker
   cd itinerary-worker    
   wrangler dev
   wrangler publish

Now you have created your own worker inside Cloudflare.


## Usage
1. Create an account in Firebase, then set up a Firestore database. Generate the environment JSON file in it, download it, and place it in your Python project directory.
2. In the project configuration file, set the following parameters: 
    NGROK_AUTH_TOKEN = "YOUR-NGROK-AUTH-TOKEN"  
    OPENAI_API_KEY = "YOUR-OPENAI-API-KEY"  
    FIREBASE_CRED_PATH = "YOUR_FIREBASE_PROJECT_DATABASE.json"  
YOUR_FIREBASE_PROJECT_DATABASE.json is the same JSON file you downloaded from the Firebase console.
3. Run the FastAPI app locally or deploy it to a server
4. By running the API, replace the phrase "NGROK_URL" in the index.ts file with the link returned to you by ngrok.
5. In the index.ts file, replace the placeholders "YOUR_FIREBASE_PROJECT_ID" and "FIRE_BASE_API_KEY" with your actual Firestore project ID and API key, which you can obtain from the Firebase console.
6. Then, in the terminal, run the command: 
   ```bash
   wrangler deploy
 By running this command, Cloudflare will return a link similar to the following:
 https://itinerary-worker.h-hosseinzade1994.workers.dev
 
7. Then, in Postman, enter the Cloudflare link and send a POST API request with the following body using the raw and JSON options.
 For example:
   ```bash
   {"destination": "Yazd, IRAN", "durationDays": 3}
8. Here, the request is first sent to Cloudflare, and then the processing begins asynchronously and the first state of the data will be saved in firestore database with processing status.
 You will receive a response similar to the following:
   ```bash
   {"jobId": "d3aa0c18-9358-458c-adc2-0334181d4985", "message": "Job created successfully"}
9. Now, this job ID is sent to FastAPI, leveraging Python's strong AI capabilities to process the request using the LLM module with prompt engineering.
  Then, the data stored in the Firestore database is updated as follows:

   ```json
   [ {
        "day": 1,
        "theme": "Explore the Historical Depths",
        "activities": [
            {
                "time": "09:00",
                "description": "Visit the Jame Mosque of Yazd, known for its stunning tile work and impressive minarets.",
                "location": "Jame Mosque of Yazd"
            },
            {
                "time": "11:00",
                "description": "Tour the Yazd Atash Behram, one of the oldest fire temples in the world.",
                "location": "Yazd Atash Behram"
            },
            {
                "time": "13:00",
                "description": "Enjoy a traditional Persian lunch at a local restaurant.",
                "location": "Local Restaurant"
            },
            {
                "time": "15:00",
                "description": "Explore the historic Fahadan neighborhood, wandering through winding alleys and admiring the architecture.",
                "location": "Fahadan Neighborhood"
            },
            {
                "time": "18:00",
                "description": "Visit the Zoroastrian Towers of Silence for a glimpse into ancient burial practices.",
                "location": "Towers of Silence"
            },
            {
                "time": "20:00",
                "description": "Dinner at a rooftop restaurant with views over Yazd's skyline.",
                "location": "Rooftop Restaurant"
            }
        ]
    },
    {
        "day": 2,
        "theme": "Cultural Immersion and Local Craft",
        "activities": [
            {
                "time": "09:00",
                "description": "Visit the Yazd Water Museum to learn about traditional water management systems.",
                "location": "Yazd Water Museum"
            },
            {
                "time": "11:00",
                "description": "Stop by the local Bazaar to shop for handicrafts, spices, and souvenirs.",
                "location": "Yazd Bazaar"
            },
            {
                "time": "13:00",
                "description": "Have lunch at a restaurant that specializes in Yazdi desserts.",
                "location": "Dessert Restaurant"
            },
            {
                "time": "15:00",
                "description": "Participate in a workshop to learn traditional carpet weaving techniques.",
                "location": "Carpet Workshop"
            },
            {
                "time": "18:00",
                "description": "Attend a cultural performance showcasing local music and dance.",
                "location": "Cultural Center"
            },
            {
                "time": "20:00",
                "description": "Dinner at a local eatery sampling Yazdi cuisine.",
                "location": "Local Eatery"
            }
        ]
    },
    {
        "day": 3,
        "theme": "Adventure and Nature",
        "activities": [
            {
                "time": "07:00",
                "description": "Early morning departure for a day trip to the Dasht-e Kavir desert.",
                "location": "Dasht-e Kavir"
            },
            {
                "time": "09:00",
                "description": "Explore the stunning landscapes, including sand dunes and salt flats.",
                "location": "Desert Landscape"
            },
            {
                "time": "12:00",
                "description": "Picnic lunch in the desert, experiencing the tranquility of the surroundings.",
                "location": "Desert Picnic Spot"
            },
            {
                "time": "14:00",
                "description": "Continue exploring and visiting local wildlife or rare flora.",
                "location": "Desert Wildlife Spot"
            },
            {
                "time": "17:00",
                "description": "Return to Yazd and relax at a traditional caravanserai.",
                "location": "Traditional Caravanserai"
            },
            {
                "time": "19:00",
                "description": "Farewell dinner featuring delightful local dishes.",
                "location": "Farewell Restaurant"
            }
        ]
    }
]
