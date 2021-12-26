using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Cinemachine;

public class MainMenu : MonoBehaviour
{
    private Animator anim;
    [SerializeField] CinemachineVirtualCamera vcam1, vcam2;


    public void PlayRoom1()
    {
        
        switchPriority();
        anim = vcam2.GetComponent<Animator>();
        anim.SetTrigger("Start");

        //yield return new WaitForSeconds(5);
        
        //SceneManager.LoadScene("Room1", LoadSceneMode.Single);
        //Time.timeScale = 1f;
    }
    /*
    public void PlayRoom2()
    {
        SceneManager.LoadScene("Room2", LoadSceneMode.Single);
        Time.timeScale = 1f;
    }
    */

    private void switchPriority()
    {
        vcam1.Priority = 0;
        vcam2.Priority = 1;
    }

    public void Quit()
    {
        Application.Quit();
    }
}
