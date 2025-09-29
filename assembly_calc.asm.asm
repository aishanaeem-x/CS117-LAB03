section .data
    msgAdd db "Addition Result: ", 0xA
    msgAddLen equ $ - msgAdd

    msgMul db "Multiplication Result: ", 0xA
    msgMulLen equ $ - msgMul

section .bss
    addResult resb 1
    mulResult resb 2

section .text
    global _start

_start:
    mov al, 4
    mov bl, 2
    add al, bl
    add al, '0'
    mov [addResult], al

    mov eax, 4
    mov ebx, 1
    mov ecx, msgAdd
    mov edx, msgAddLen
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, addResult
    mov edx, 1
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, msgAdd+msgAddLen-1
    mov edx, 1
    int 0x80

    mov al, 4
    mov bl, 2
    mul bl
    add al, '0'
    mov [mulResult], al

    mov eax, 4
    mov ebx, 1
    mov ecx, msgMul
    mov edx, msgMulLen
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, mulResult
    mov edx, 1
    int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80