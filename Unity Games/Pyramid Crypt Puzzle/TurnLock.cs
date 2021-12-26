using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class TurnLock : MonoBehaviour
{
    [SerializeField] GameObject gate, cat1, cat2, cat3;

    public int turnCode, attemptedCode;
    public bool canTurn = true;

    public int cat1pos, cat2pos, cat3pos = 1;

    public void setCodes(int in_turnCode)
    {
        this.turnCode = in_turnCode;
    }


    void CheckCode()
    {
        if (attemptedCode == turnCode)
        {
            Open();
            FindObjectOfType<AudioManager>().Play("CompletePuzzle");

        }
        else
        {
            //Debug.Log("Wrong Code");
        }
    }

    public void Open()
    {
        Animator anim = gate.GetComponent<Animator>();
        AudioSource audioData = cat2.GetComponent<AudioSource>();
        audioData.Play(0);
        anim.SetTrigger("GateOpen");
        canTurn = false;

    }

    public int GetPos(string name)
    {
        if(name == "catOne")
        {
            return cat1pos;
        }

        if(name == "catTwo")
        {
            return cat2pos;
        }

        if(name == "catThree")
        {
            return cat3pos;
        }
        else
        {
            return -1;
        }
    }

    public void Turn(string name)
    {
        switch (name)
        {
            case "catOne":
                cat1pos++;
                if (cat1pos == 5)
                {
                    cat1pos = 1;
                }

                break;

            case "catTwo":
                cat2pos++;
                if (cat2pos == 5)
                {
                    cat2pos = 1;
                }

                break;

            case "catThree":
                cat3pos++;
                if (cat3pos == 5)
                {
                    cat3pos = 1;
                }

                break;

            default:
                Debug.Log("cat statue error");
                break;
        }
        SetValue(cat1pos, cat2pos, cat3pos);
    }

    public void SetValue(int cat1, int cat2, int cat3)
    {

        attemptedCode = ((cat1 * 100) + (cat2 * 10) + cat3);
        CheckCode();

        attemptedCode = 0;
    }
}
