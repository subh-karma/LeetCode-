package assignment3;

import java.io.*;

class Game implements Serializable {
    String game_name;
    int no_of_players;

    public Game(String game_name, int no_of_players) {
        this.game_name = game_name;
        this.no_of_players = no_of_players;
    }

    @Override
    public String toString() {
        return "Game [game_name=" + game_name + ", no_of_players=" + no_of_players + "]";
    }
}

public class SerializationExample {
    public static void main(String[] args) {
        // Create 5 Game objects
        Game[] games = new Game[5];
        games[0] = new Game("Chess", 2);
        games[1] = new Game("Monopoly", 4);
        games[2] = new Game("Scrabble", 4);
        games[3] = new Game("Risk", 6);
        games[4] = new Game("Settlers of Catan", 4);

        // Serialize the Game objects to a file
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("games.ser"))) {
            for (Game game : games) {
                out.writeObject(game);
            }
            System.out.println("Games serialized successfully!");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

        // Deserialize the Game objects from the file and display them
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("games.ser"))) {
            for (int i = 0; i < 5; i++) {
                Game game = (Game) in.readObject();
                System.out.println(game);
            }
            System.out.println("Games deserialized successfully!");
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error reading from file: " + e.getMessage());
        }
    }
}
