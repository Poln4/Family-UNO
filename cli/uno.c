#include <stdio.h>
#include <cs50.h>
#include <string.h>

// Max points and players
#define MAX_POINTS 200
#define MAX_PLAYERS 9

// Players have name, points count, eliminated status
typedef struct
{
    string name;
    int points;
    bool eliminated;
}
player;

// Array of players
player players[MAX_PLAYERS];

// Numbers of points and players
int points_count;
int players_count;
bool game;

// Function prototypes
void print_winner(int min);
int find_min(void);

int main(int argc, string argv[])
{
  // Check for invalid usage
    if (argc < 2)
    {
        printf("Uso: uno [jugadores ...]\n");
        return 1;
    }
    // Populate array of players
    players_count = argc - 1;
    if (players_count > MAX_PLAYERS)
    {
        printf("Maximum number of players is %i\n", MAX_PLAYERS);
        return 2;
    }
    for (int i = 0; i < players_count; i++)
    {
        players[i].name = argv[i + 1];
        players[i].points = 0;
        players[i].eliminated = false;
    }
        // Keep querying for votes
    game = true;
    int i = 1;
    while (game)
    {
        printf("Ronda %i\n", i);

        // Query for each player
        for (int j = 0; j < players_count; j++)
        {
            int points = get_int("Puntos %s: ", players[j].name);
            players[j].points += points;

        }
        printf("\n");
        for (int t = 0; t < players_count; t++)
        {
            printf("%s tiene %i puntos.\n", players[t].name, players[t].points);
        }
        printf("\n");
        for (int k = 0; k < players_count; k++)
        {
            if (players[k].points >= MAX_POINTS)
            {
                players[k].eliminated = true;
                printf("%s ha perdido con %i puntos.\n", players[k].name, players[k].points);
                game = false;
                break;
            }
        }
        i++;
        printf("\n");
    }

     // Find the player with less points
    int min = find_min();

     // Prints the winner and everyone's points
    print_winner(min);
    printf("\n");
    for (int p = 0; p < players_count; p++)
        {
            printf("%s obtuvo  %i puntos.\n", players[p].name, players[p].points);

        }
        printf("\n");
}


int find_min(void)
{
    // Copies the points into an array
    int arr[players_count];
    int valid_points = players_count;

    for (int i = 0; i < players_count; i++)
    {
        arr[i] = players[i].points;
    }

    //con los puntos listos, hay que ordenar la lista, para así obtener el resultado mínimo que estará en el index 0
    for (int k = 0; k < players_count; k++)
    {
        for (int j = k + 1; j < valid_points; j++)
        {
            if (arr[k] > arr[j])
            {
                int temp = arr[k];
                arr[k] = arr[j];
                arr[j] = temp;
            }
        }
    }
    int p = 0;
    for (int j = 0; j < players_count; j++)
    {
        if (players[j].points == arr[0])
        {
            p = j;
        }
    }
    return p;
}

void print_winner(int min)
{
    printf("¡%s ha ganado!\n", players[min].name);
}

