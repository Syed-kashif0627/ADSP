#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source_file> <destination_file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int src_fd, dest_fd;
    char buffer[4096];
    ssize_t bytes_read, bytes_written;

    // Open the source file in read-only mode
    src_fd = open(argv[1], O_RDONLY);
    if (src_fd == -1) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    // Create (or truncate) the destination file in write-only mode
    dest_fd = open(argv[2], O_WRONLY | O_CREAT, 0644);
    if (dest_fd == -1) {
        perror("Error opening/creating destination file");
        close(src_fd);
        exit(EXIT_FAILURE);
    }

    // Copy file contents
    while ((bytes_read = read(src_fd, buffer, sizeof(buffer))) > 0) {
        bytes_written = write(dest_fd, buffer, bytes_read);
        if (bytes_written != bytes_read) {
            perror("Error writing to destination file");
            close(src_fd);
            close(dest_fd);
            exit(EXIT_FAILURE);
        }
    }

    if (bytes_read == -1) {
        perror("Error reading source file");
    }

    // Close file descriptors
    close(src_fd);
    close(dest_fd);

    printf("File copied successfully.\n");
    return 0;
}
