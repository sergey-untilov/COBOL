       IDENTIFICATION DIVISION.
       PROGRAM-ID. app.
      *
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           01  args    PIC X(50).
           01  args0   PIC X(51).
      *
       PROCEDURE DIVISION.
           ACCEPT args FROM COMMAND-LINE.
      *    ACCEPT args FROM STDIN
           String args delimited by size
            X'00' delimited by size
            into args0.
           call "shared_print" using by reference args0.
           stop run.
