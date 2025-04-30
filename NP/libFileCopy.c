#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source_file> <destination_file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    FILE *src, *dest;
    char buffer[4096]; // Buffer to hold data during transfer
    size_t bytes;

    // Open the source file in read mode
    src = fopen(argv[1], "rb");
    if (src == NULL) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    // Open the destination file in write mode
    dest = fopen(argv[2], "wb");
    if (dest == NULL) {
        perror("Error opening destination file");
        fclose(src); // Close the source file before exiting
        exit(EXIT_FAILURE);
    }

    // Copy contents from source to destination
    while ((bytes = fread(buffer, 1, sizeof(buffer), src)) > 0) {
        if (fwrite(buffer, 1, bytes, dest) != bytes) {
            perror("Error writing to destination file");
            fclose(src);
            fclose(dest);
            exit(EXIT_FAILURE);
        }
    }

    // Close both files
    fclose(src);
    fclose(dest);

    printf("File copied successfully.\n");
    return 0;
}
