import java.util.regex.Pattern;
import java.util.regex.Matcher;

// TODO : NO EJECUTAR

public class clase {
    public static boolean useRegex(final String input) {
        // Compile regular expression
        final Pattern pattern = Pattern.compile("^\\+[0-9]*\\.[0-9]+$", Pattern.CASE_INSENSITIVE);
        // Match regex against input
        final Matcher matcher = pattern.matcher(input);
        // Use results...
        return matcher.matches();
    }

    public static void main(String[] args) {
        System.out.println(useRegex("+123.456")); // true
        System.out.println(useRegex("+123.456.789")); // false
        System.out.println(useRegex("+123")); // false
        System.out.println(useRegex("+123.")); // false
        System.out.println(useRegex("+.456")); // false
        System.out.println(useRegex("+.456.")); // false
        System.out.println(useRegex("+")); // false
        System.out.println(useRegex("+.")); // false
        System.out.println(useRegex("123.456")); // false
        System.out.println(useRegex("123.456.")); // false
        System.out.println(useRegex("123")); // false
        System.out.println(useRegex("123.")); // false
        System.out.println(useRegex(".456")); // false
        System.out.println(useRegex(".456.")); // false
        System.out.println(useRegex("")); // false
        System.out.println(useRegex(".")); // false
    }
}