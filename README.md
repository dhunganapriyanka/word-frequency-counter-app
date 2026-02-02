## Overview
This program analyzes word frequencies using multiple threads. It splits a text file into N parts, assigns each part to a separate thread, and counts the words in parallel. After all threads finish their work, the main thread combines the results into a single, final word-frequency summary.

## Features
- Accepts a **text file** as input
- Accepts the **number of segments (N)** as a command line parameter
- Uses **multithreading** to process file at the same time
- Generates **word-count result** for each thread
- Combines the result into a **final one consolidated word-frequency output**

## Requirements
- Python 3.x

## How to Run
1. Install Python on your computer.
2. Place your text file (`sample.txt`) in the same folder as `word_frequency.py`.
3. Open a terminal and navigate to the project folder.
4. Run the program:
   ```
   python word_frequency.py
   ```
5. When prompted, enter the text file name and the number of segments as input:
   ```
   Enter the text file name: sample.txt
   Enter number of segments (threads): 3
   ```
6. The program will display the segments, each thread's word count, and the final combined word frequencies.
