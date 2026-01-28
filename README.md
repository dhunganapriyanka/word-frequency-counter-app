## Overview
This program demonstrates **multithreaded word-frequency analysis**. A text file is divided into **N segments**, each processed concurrently by a separate thread to compute word counts. Once all threads finish, the main thread **merges the results** into a final consolidated word-frequency count.

## Features
- Accepts a **text file** as input  
- Accepts the **number of segments (N)** as a parameter  
- Uses **multithreading** for concurrent processing  
- Generates **intermediate word-frequency counts** per thread  
- Produces a **final consolidated word-frequency output**
