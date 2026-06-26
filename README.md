# AI From Scratch + Video & Sound Reader — Python Roadmap

**The honest scope note first:** "from scratch" means two different things depending on the layer.

- **The intelligence layer (neural nets, learning, backprop)** — we build this for real, with nothing but numpy. This is where "from scratch" actually matters and is achievable in weeks.
- **The decoding layer (turning a video file into pixels, an audio file into numbers)** — writing your own MP4/H.264/WAV parser is a multi-year specialist field on its own. We use OpenCV and Python's `wave`/`librosa` here, the same way you use Python's `import` instead of writing your own compiler. You'll still deeply understand *how* video/audio becomes data — you just won't hand-roll the codec.

Go level by level. Don't skip Level 3 — it's the foundation everything else sits on.

---

## Level 0 — Python Foundations
**Goal:** comfort with the language itself.
- `print`, `input`, variables, types
- `if`/`else`, `for`/`while` loops
- functions, parameters, `*args`/`**kwargs`, scope
- lists, dicts, tuples, sets, comprehensions
- string formatting (f-strings)
- file I/O: `open()`, read/write/append
- `try`/`except` error handling
- `pip`, virtual environments, importing modules

**Mini projects:**
- Number guessing game
- CLI to-do list that saves to a text file
- Simple journal app (append-only file log with timestamps)

---

## Level 1 — Intermediate Python & OOP
**Goal:** structure and the two libraries you'll live in: numpy and matplotlib.
- classes, objects, inheritance, `__init__`/`__repr__`/dunder methods
- decorators, generators, context managers (`with`)
- reading/writing JSON
- numpy: arrays, shape, dtype, broadcasting, vectorized math (no loops!)
- matplotlib: plotting arrays, images, simple graphs

**Mini projects:**
- Bank account class system (deposit/withdraw/transfer, with history)
- CSV analyzer: load a dataset with numpy, plot a couple of charts

---

## Level 2 — The Math, in Code
**Goal:** the minimum math to understand learning, taught by writing it.
- vectors & matrices as numpy arrays
- dot products, matrix multiplication
- derivatives & chain rule (conceptual, then a tiny coded example)
- gradient descent: minimize a function by walking downhill

**Mini project:**
- Write gradient descent from scratch to find the minimum of `y = x²`, then a 2-variable bowl-shaped function. Plot the descent path.

---

## Level 3 — Build a Neural Network From Scratch (pure numpy)
**Goal:** this is the actual "AI from scratch" milestone.
- the neuron: weights, bias, activation functions (sigmoid, ReLU)
- forward propagation, by hand
- loss functions (MSE, cross-entropy)
- backpropagation — derive it, then code it (no autograd, no shortcuts)
- training loop: epochs, batch size, learning rate

**Mini projects:**
- Perceptron that learns AND / OR / XOR
- 2-layer network that classifies handwritten digits (MNIST), using only numpy — no PyTorch, no TensorFlow

---

## Level 4 — Reading Images in Python
**Goal:** understand that an image is just numbers before you feed it to anything.
- images as arrays: pixels, RGB channels, grayscale
- Pillow (`PIL`): open, resize, convert, save
- manual array math as filters: blur, edge detection, brightness

**Mini project:**
- Build 3 image filters using only raw numpy array math (don't use cv2's built-in filter functions — write the math yourself)

---

## Level 5 — The Video Reading App
**Goal:** the literal "split a video into every frame" tool.
- a video = sequence of frames + a frame rate (fps)
- OpenCV `cv2.VideoCapture`: read frame by frame, get frame count/fps
- saving frames as individual images

**Mini project:**
- CLI tool: `python extract.py video.mp4 --every 5` → dumps every 5th frame to a folder as `.png`, with a progress counter

---

## Level 6 — Teaching Your Network to "Watch"
**Goal:** connect Level 3's brain to Level 5's eyes.
- feed extracted frames into your numpy network (resize + flatten frames first)
- why plain numpy struggles with images at real scale (conceptual intro to convolution)
- optional but worth it: hand-code one convolution operation in numpy, just to *see* how it works
- pragmatic pivot: once you understand convolution by hand, swap to PyTorch/TensorFlow for the actual frame classifier — this is the point where hand-rolled numpy becomes too slow to be useful, and that's fine

**Mini project:**
- A script that walks through a video frame by frame and classifies each one (e.g. "cat" vs "no cat" — train on a small labeled set of frames you collect yourself)

---

## Level 7 — Reading Sound
**Goal:** realize audio is the same trick as images.
- sound = waveform: samples, sample rate, amplitude
- reading audio with Python's `wave` module, then `librosa` for convenience
- converting sound → spectrogram (this turns audio into an *image* — your image-classifying network can now "see" sound)

**Mini project:**
- Load/record a short clip, generate its spectrogram, classify simple sounds (clap vs silence vs whistle) using a network from Level 3/6

---

## Level 8 — Capstone: Multi-modal Watcher
**Goal:** put it all together.
- run your frame classifier and your sound classifier over the same clip
- combine both into a simple per-second log: what it saw + what it heard

**Mini project:**
- "Video & Sound Watcher": feed in a short clip, get back a console/log output like:
  ```
  0:00–0:02 — saw: cat | heard: silence
  0:02–0:04 — saw: cat | heard: meow-like sound
  ```

---

## Pacing notes
- No fixed timeline — go at the speed where each mini project actually works before moving on.
- Level 3 is the hinge point. If backprop feels shaky, stay there longer; everything after assumes it clicked.
- It's fine (encouraged) to revisit Level 6's "build convolution by hand" even after you've moved to PyTorch — understanding it once is the goal, not using your hand-rolled version forever.