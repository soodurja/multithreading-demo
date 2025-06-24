---

# 🧵 Python Multithreading Demo

This project demonstrates how Python handles I/O-bound tasks sequentially vs concurrently using threads. It's ideal for beginners looking to understand how multithreading improves performance in Python.

---

## 🚀 Overview

We simulate two simple I/O-bound functions:

* **Squaring** each number in a list
* **Cubing** each number in a list

Each operation includes a `1-second` delay per number to simulate I/O latency (e.g., file access, network requests).

Two implementations are provided:

* `no_multithreading.py` – executes tasks **sequentially**
* `with_multithreading.py` – executes tasks **concurrently** using threads

---

## 📁 Project Structure

```
Multithreading/
│
├── .gitignore                 ← Git config to ignore venv, etc.
├── LICENSE                    ← Project license
├── README.md                  ← You are here
├── no_multithreading.py       ← Sequential version: squaring & cubing one after the other
└── with_multithreading.py     ← Threaded version: runs squaring & cubing in parallel
```

---

## 🧪 Sample Output

This project compares two approaches to running the same task — one without multithreading (sequential execution) and the other with multithreading (concurrent execution). By comparing the outputs, we observe how multithreading helps reduce execution time by allowing parallelism.

### 🔴 Without Multithreading

```
C:\Users\soodu\PycharmProjects\Multithreading\venv\Scripts\python.exe C:\Users\soodu\PycharmProjects\Multithreading\no_multithreading.py 
Squaring the number 1
Squaring the number 2
Squaring the number 3
Squaring the number 4
Cubing the number 1
Cubing the number 2
Cubing the number 3
Cubing the number 4
Squared list: [1, 4, 9, 16]
Cubed list: [1, 8, 27, 64]
Time taken: 8.060130834579468

Process finished with exit code 0
```

### 🟢 With Multithreading

```
C:\Users\soodu\PycharmProjects\Multithreading\venv\Scripts\python.exe C:\Users\soodu\PycharmProjects\Multithreading\with_multithreading.py 
Squaring the number 1
Cubing the number 1

Cubing the number 2
Squaring the number 2
Squaring the number 3
Cubing the number 3
Squaring the number 4
Cubing the number 4
Squared list: [1, 4, 9, 16]
Cubed list: [1, 8, 27, 64]
Time taken: 4.035823106765747

Process finished with exit code 0
```


This project demonstrates the impact of multithreading by comparing two versions of the same program — one using sequential execution and the other using concurrent threads. The multithreaded version completes in approximately 4 seconds, while the non-threaded version takes around 8 seconds. This reduction in execution time highlights how multithreading improves performance by overlapping I/O-bound tasks, such as delays, through parallel execution.

---

## 🌐 Real-World Relevance

Multithreading allows Python to run multiple I/O-bound operations concurrently — saving time and improving responsiveness. This is especially useful in:

* File processing
* Web scraping
* Network requests
* UI applications

---

## 🛠 How to Run

1. **Clone the repository**

```
git clone https://github.com/soodurja/multithreading-demo.git
cd Multithreading
```

2. **Run each script**

```
python no_multithreading.py
python with_multithreading.py
```

Observe the **difference in execution time** and how logs interleave in the multithreaded version.

---

## 🧠 Conclusion

This simple project offers a hands-on comparison of how multithreading helps with I/O-bound performance in Python. It’s a valuable building block before exploring advanced concepts like multiprocessing, asyncio, or thread pools.

---
