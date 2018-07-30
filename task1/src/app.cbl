       IDENTIFICATION DIVISION.
       PROGRAM-ID. app.
      *
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           01  args    PIC X(50).
      *
       PROCEDURE DIVISION.
           ACCEPT args FROM COMMAND-LINE.
      *    ACCEPT args FROM STDIN
           call "shared_print" using by reference args.
           stop run.
