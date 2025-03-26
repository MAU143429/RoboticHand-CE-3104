# 🤖 Robotic Hand Compiler Project — CE3104

## 📘 Overview

This repository contains the complete implementation of a custom programming language, its compiler, and its integration with a robotic hand, developed as part of the course CE3104 – Lenguajes, Compiladores e Intérpretes at Instituto Tecnológico de Costa Rica.

The goal of the project was to design a new language with its own IDE and compiler, and use it to control a physical robotic hand constructed with servomotors and custom circuits.

---

## 🛠️ Main Components

### 🧠 Compiler
- Built in **Python 3** using the **PLY** (Python Lex-Yacc) library
- Includes:
  - Lexical analyzer
  - Syntax parser
  - Semantic checker
- Compiles high-level instructions into a format understandable by the Arduino microcontroller
- Error detection for:
  - Multiple `main` definitions
  - Undeclared variables
  - Invalid parameter passing

### ✋ Robotic Hand
- Built with a **wooden structure** and **servo-driven fingers**
- Controlled by an **Arduino UNO**
- Commands are sent from the compiler to the board via **serial communication** using `pyserial`
- Each finger emits a unique **sound** when activated

---

## ⚙️ Requirements

- Python 3.6+
- PLY 3.11
- Pyserial 3.5
- Arduino IDE 1.8.15
- Compatible microcontroller (e.g., Arduino UNO)
- Fully assembled robotic hand and circuit

---

## 📌 Notes

This project merges the theoretical concepts of compiler construction with hands-on embedded systems, offering a unique multidisciplinary experience in both software and hardware development.

