// #include <stdio.h>
// #include <stdlib.h>
// #include <sys/stat.h>
// #include <pwd.h>
// #include <grp.h>
// #include <time.h>

// int main(int argc, char *argv[]) {
//     if (argc != 2) {
//         fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
//         exit(EXIT_FAILURE);
//     }

//     struct stat fileStat;
//     if (stat(argv[1], &fileStat) == -1) {
//         perror("Error retrieving file information");
//         exit(EXIT_FAILURE);
//     }

//     // File type
//     printf("File Type: ");
//     if (S_ISREG(fileStat.st_mode))
//         printf("Regular file\n");
//     else if (S_ISDIR(fileStat.st_mode))
//         printf("Directory\n");
//     else if (S_ISCHR(fileStat.st_mode))
//         printf("Character device\n");
//     else if (S_ISBLK(fileStat.st_mode))
//         printf("Block device\n");
//     else if (S_ISFIFO(fileStat.st_mode))
//         printf("FIFO (pipe)\n");
//     else if (S_ISLNK(fileStat.st_mode))
//         printf("Symbolic link\n");
//     else if (S_ISSOCK(fileStat.st_mode))
//         printf("Socket\n");
//     else
//         printf("Unknown type\n");

//     // Number of hard links
//     printf("Number of Hard Links: %ld\n", fileStat.st_nlink);

//     // Last access time
//     printf("Last Access Time: %s", ctime(&fileStat.st_atime));

//     // User name
//     struct passwd *user = getpwuid(fileStat.st_uid);
//     if (user != NULL)
//         printf("User Name: %s\n", user->pw_name);
//     else
//         printf("User Name: Unknown\n");

//     // Group name
//     struct group *grp = getgrgid(fileStat.st_gid);
//     if (grp != NULL)
//         printf("Group Name: %s\n", grp->gr_name);
//     else
//         printf("Group Name: Unknown\n");

//     return 0;

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    struct stat fileStat;
    if (stat(argv[1], &fileStat) == -1) {
        perror("Error retrieving file information");
        exit(EXIT_FAILURE);
    }

    // File type
    printf("File Type: ");
    if (S_ISREG(fileStat.st_mode))
        printf("Regular file\n");
    else if (S_ISDIR(fileStat.st_mode))
        printf("Directory\n");
    else if (S_ISCHR(fileStat.st_mode))
        printf("Character device\n");
    else if (S_ISBLK(fileStat.st_mode))
        printf("Block device\n");
    else if (S_ISFIFO(fileStat.st_mode))
        printf("FIFO (pipe)\n");
    else
        printf("Unknown type\n");

    // Number of hard links
    printf("Number of Hard Links: %ld\n", fileStat.st_nlink);

    // Last access time
    printf("Last Access Time: %s", ctime(&fileStat.st_atime));

    return 0;
}

