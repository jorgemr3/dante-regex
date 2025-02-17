import java.util.regex.Pattern;
import java.util.regex.Matcher;

// TODO : NO EJECUTAR

public class main {
    public static boolean useRegex(final String input) {
        // Compile regular expression
        final Pattern pattern = Pattern.compile("^\\+[0-9]*\\.[0-9]+$", Pattern.CASE_INSENSITIVE);
        // Match regex against input
        final Matcher matcher = pattern.matcher(input);
        // Use results...
        return matcher.matches();
    }
}