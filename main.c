#include <regex.h>

// TODO : NO SE PUEDE EJECUTAR

int useRegex(char* textToCheck) {
    regex_t compiledRegex;
    int reti;
    int actualReturnValue = -1;
    char messageBuffer[100];

    /* Compile regular expression */
    reti = regcomp(&compiledRegex, "^[+-]?(?=\d+\.?\d*$|\.?\d+)(\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?$", REG_EXTENDED | REG_ICASE);
    // solo primer regex
    if (reti) {
        fprintf(stderr, "Could not compile regex\n");
        return -2;
    }

    /* Execute compiled regular expression */
    reti = regexec(&compiledRegex, textToCheck, 0, NULL, 0);
    if (!reti) {
        puts("Match");
        actualReturnValue = 0;
    } else if (reti == REG_NOMATCH) {
        puts("No match");
        actualReturnValue = 1;
    } else {
        regerror(reti, &compiledRegex, messageBuffer, sizeof(messageBuffer));
        fprintf(stderr, "Regex match failed: %s\n", messageBuffer);
        actualReturnValue = -3;
    }

    /* Free memory allocated to the pattern buffer by regcomp() */
    regfree(&compiledRegex);
    return actualReturnValue;
}