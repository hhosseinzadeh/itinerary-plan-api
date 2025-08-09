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
 
4. then write this command in your system terminal:
   ```bash
   wrangler login
   wrangler generate itinerary-worker
   cd itinerary-worker    
   wrangler dev
   wrangler publish
