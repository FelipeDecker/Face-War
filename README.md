# Face War

Face War is a 2D arcade-style action game developed in Python with Pygame. The player controls a happy face in a desert setting, dodges enemies crossing the screen, and fires projectiles to destroy them.

## About the project

The game runs in an 840 x 480 pixel window. The character remains on the left side of the screen while enemies appear randomly outside the right edge and move toward the player. The game continues until the character collides with an enemy.

When a shot hits an asteroid, both sprites are removed. When an asteroid hits the player, the game enters the game over state, plays the corresponding sound, and prints `Game Over` in the terminal.

## How to play

### Running from the source code

1. Install Python 3.
2. Install the project dependency:

   ```bash
   pip install pygame
   ```

3. Open a terminal in the project folder.
4. Run:

   ```bash
   python app.py
   ```

The files in the `Resources/` folder must remain in the same relative location because the game loads images and sounds using these paths.

### Running the compiled version

The repository also includes `app.exe`, which can be run directly on Windows. The visual and audio resources must still be available according to the distributed project structure.

## Controls

| Key              | Action               |
| ---------------- | -------------------- |
| `W`              | Move the player up   |
| `S`              | Move the player down |
| `Space`          | Fire a projectile    |
| Close the window | Exit the game        |

Movement uses acceleration: when `W` or `S` is pressed, the speed gradually increases. When neither key is pressed, the speed progressively decreases, creating a deceleration effect. The character is restricted to the top and bottom boundaries of the window.

## Mechanics

- The window is updated at 60 frames per second.
- Asteroids appear periodically, with an 80% chance at each spawn cycle.
- Each asteroid receives a random vertical position and a random speed between approximately 2 and 4 pixels per frame.
- Asteroids that leave the screen through the left edge are removed from the game.
- Each shot travels horizontally to the right at 5 pixels per frame.
- Shots that pass the right edge of the window are removed.
- Collisions between the player and asteroids, and between shots and asteroids, use `pygame.sprite.collide_mask`, allowing shape-based sprite collision detection.
- Background music loops during execution.
- Separate sounds are used for shots and game over.

## Project structure

```text
Face-War/
|-- app.py                 # Initialization, main loop, and game rules
|-- player.py              # Player sprite and movement
|-- asteroid.py            # Enemy creation, movement, and removal
|-- shot.py                # Shot creation, movement, and removal
|-- README.md              # Project documentation
|-- TODO.md                # Pending tasks and future improvements
|-- Aluno.txt              # Student identification
|-- app.exe                # Windows executable version
`-- Resources/             # Images and audio files
```

### Python file responsibilities

#### `app.py`

Initializes Pygame, creates the window, loads the background and sounds, creates the sprite groups, and controls the main loop. It also processes keyboard events, spawns asteroids, updates objects, draws the scene, and handles collisions.

#### `player.py`

Defines the `Player` class, which inherits from `pygame.sprite.Sprite`. The character uses `HappyFace.png`, has a size of 100 x 100 pixels, and controls its vertical position with acceleration and deceleration.

#### `asteroid.py`

Defines the `Asteroid` class. The enemy uses `RedGuy.png`, has a size of 50 x 50 pixels, appears outside the right side of the window, and moves to the left. It is destroyed when it leaves the screen.

#### `shot.py`

Defines the `Shot` class. The projectile uses `Shot.png`, has a size of 20 x 20 pixels, and moves to the right. It is removed when it leaves the window.

## Resources

| File                  | Usage                                             |
| --------------------- | ------------------------------------------------- |
| `Desert.png`          | Main background, scaled to 840 x 480              |
| `HappyFace.png`       | Player image                                      |
| `RedGuy.png`          | Asteroid/enemy image                              |
| `Shot.png`            | Projectile image                                  |
| `BackgroundSound.mp3` | Looping background music                          |
| `swing.wav`           | Shooting sound                                    |
| `GameOver.wav`        | Collision/game over sound                         |
| `Background.jpg`      | Additional visual resource included in the folder |
| `battleThemeA.mp3`    | Additional audio resource included in the folder  |
| `Destroyed.wav`       | Additional audio resource included in the folder  |

The last three files are included in the repository but are not currently loaded by `app.py`.

## Technologies used

- **Python 3:** Programming language used for the implementation.
- **Pygame:** Library responsible for the window, event loop, sprites, groups, images, audio, keyboard input, collisions, and time control.
- **Random:** Standard library module used to choose positions, speeds, and the asteroid spawn chance.
- **OS and Sys:** Standard library modules used to resolve the execution directory and support packaged execution, including the executable version.
- **PyInstaller or an equivalent tool:** The presence of `app.exe` indicates a compiled Windows distribution; the packaging command is not recorded in the repository.

## Planning

The checklist of tasks needed to complete the project and the list of future improvements are available in [TODO.md](TODO.md).
