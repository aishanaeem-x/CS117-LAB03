# CS117-LAB03
# Reflections on Assembly and Python

## 1. Assembly Reflections

- **What did you notice about registers and instructions?**  
Registers like eax, ebx, ecx are used in assembly to store data. Registers are very limited in number and size, and each instruction operates directly on them. Assembly uses low level instructions for the code.

- **How is coding in Assembly different from Python?**  
  Assembly is very low-level and requires attention to hardware details, while Python is high-level. In Assembly, even simple operations take multiple lines of code, while Python can achieve the same with one statement. Assembly is closer to machine code, while Python is more easily readable.

---

## 2. Python Reflections

- **Why is Python easier/faster for building the same project?**
  python is easier beacuse it has built-in functions and a large standard library which stores predefined functions and makes it easier to code whereas assembly would require more detail.

- **Which features of Python help abstraction (variables, functions, loops)?**  
  - **Variables:** Allow data storage without worrying about low-level memory management.  
  - **Functions:** Enable modular code, reusability, and cleaner structure.  
  - **Loops:** Simplify repetitive tasks, avoiding manual repetition of instructions.  
## 3.Comparison table
## 3. Comparison Table

| Feature          | Assembly Example | Python Example | Notes |
|------------------|------------------|----------------|-------|
| Variable storage | Register (EAX)   | `x = 5`        | Python handles memory automatically, while Assembly needs manual handling. |
| Printing output  | `INT 21h`        | `print()`      | Python has a simple built-in print function. Assembly uses system interrupts. |
| Arithmetic       | `ADD AX, BX`     | `x + y`        | Python uses the `+` operator directly. Assembly needs specific instructions. |


