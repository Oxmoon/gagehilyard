using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PauseMenu : MonoBehaviour
{
    public static bool gameIsPaused = false;
    public GameObject pauseMenuUI, crosshair;
    private GameManager gameManager;


    void Start()
    {
        gameManager = FindObjectOfType<GameManager>();
    }
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape) && gameManager.creditsPlaying != true)
        {
            if (gameIsPaused)
            {
                Resume();
            }
            else
            {
                Pause();
            }
        }
        
        else if (Input.anyKeyDown && gameManager.canLeave == true)
        {
            PlayMainMenu();
        }
        
    }

    public void Resume()
    {
        pauseMenuUI.SetActive(false); 
        Time.timeScale = 1f;
        crosshair.SetActive(true);
        Cursor.lockState = CursorLockMode.Locked;
        gameIsPaused = false;
    }

    void Pause()
    {
        pauseMenuUI.SetActive(true);
        Time.timeScale = 0f;
        crosshair.SetActive(false);
        Cursor.lockState = CursorLockMode.None;
        gameIsPaused = true;

    }
    public void PlayMainMenu()
    {
        if(gameIsPaused == true)
        {
            Resume();
        }
        Cursor.lockState = CursorLockMode.None;
        SceneManager.LoadScene("MenuTerrain");
    }

    public void Reload()
    {
        SceneManager.LoadScene("Room1", LoadSceneMode.Single);
        Resume();
    }
}
