import java.util.*;
import java.io.*;

public class Sanat {
    public static void main(String[] args) throws Exception {
        Scanner lukija1 = new Scanner(new File("suomi.txt"));
        Scanner lukija2 = new Scanner(new File("englanti.txt"));
        ArrayList<String> suomenSanat = new ArrayList<>();
        while (lukija1.hasNext()) {
            String sana = lukija1.next();
            suomenSanat.add(sana);
        }
        System.out.println(suomenSanat.size());
        HashSet<String> enkunSanat = new HashSet<>();
        while (lukija2.hasNext()) {
            String sana = lukija2.next();
            enkunSanat.add(sana);
        }
        System.out.println(enkunSanat.size());
        int laskuri = 0;
        for (String suomenSana : suomenSanat) {
            if (enkunSanat.contains(suomenSana)) {
                System.out.println(suomenSana);
                laskuri++;
            }
        }
        System.out.println("Yhteensä: "+laskuri);
    }
}
