using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SwitchLock : MonoBehaviour
{
    public int code = 2101;
    private int attemptedCode;
    [SerializeField] GameObject switch1, switch2, switch3, switch4, platform;
    AudioSource audioData;
    Animator anim;
    public bool canMove = true;
    private int switch1pos, switch2pos, switch3pos, switch4pos = 0;

    public void CheckCode()
    {
        if (attemptedCode == code)
        {
            Open();
            FindObjectOfType<AudioManager>().Play("CompletePuzzle");
        }
    }

    public void Open()
    {
        Animator anim = platform.GetComponent<Animator>();
        anim.SetTrigger("Rise");
        AudioSource audioData = platform.GetComponent<AudioSource>();
        audioData.Play(0);
        canMove = false;
    }

    public void Move(string name)
    {
        switch (name)
        {
            case "Switch1":
                switch1pos++;
                if (switch1pos == 3)
                {
                    switch1pos = 0;
                }

                break;

            case "Switch2":
                switch2pos++;
                if (switch2pos == 3)
                {
                    switch2pos = 0;
                }

                break;

            case "Switch3":
                switch3pos++;
                if (switch3pos == 3)
                {
                    switch3pos = 0;
                }

                break;
            
            case "Switch4":
                switch4pos++;
                if (switch4pos == 3)
                {
                    switch4pos = 0;
                }

                break;

            default:
                Debug.Log("Switch error");
                break;
        }
        SetValue(switch1pos, switch2pos, switch3pos, switch4pos);
    }
    public void SetValue(int switch1, int switch2, int switch3, int switch4)
    {

        attemptedCode = ((switch1 * 1000) + (switch2 * 100) + (switch3 * 10) + switch4);
        CheckCode();
        attemptedCode = 0;
    }

    public int GetPos(string name)
    {
        if(name == "Switch1")
        {
            return switch1pos;
        }

        if(name == "Switch2")
        {
            return switch2pos;
        }

        if(name == "Switch3")
        {
            return switch3pos;
        }
        if(name == "Switch4")
        {
            return switch4pos;
        }
        else
        {
            return -1;
        }
    }
}
