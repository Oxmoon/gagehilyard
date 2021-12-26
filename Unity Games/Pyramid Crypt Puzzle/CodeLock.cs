using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class CodeLock : MonoBehaviour
{
    [SerializeField] GameObject door, finalDoor;
    [SerializeField] GameObject torches;
    private Animator groupAnim;
    private AudioSource audioData;
    int placeInCode;
    public string code1, code2 = "";
    public string attemptedCode;
    private int codeLength = 3;

    public void setCodes(string in_code1, string in_code2)
    {
        this.code1 = in_code1;
        this.code2 = in_code2;
    }
    void CheckCode()
    {
        if (attemptedCode == code1)
        {
            Open1();
        }
        else if (attemptedCode == code2)
        {
            Open2();
            TurnOnTorches();
        }
        else
        {
            //Debug.Log("Wrong Code");
        }
    }

    public void Open1()
    {
        Animator anim1 = door.GetComponent<Animator>();
        audioData = door.GetComponent<AudioSource>();
        audioData.Play(0);
        anim1.SetTrigger("DoorOpen");
        FindObjectOfType<AudioManager>().Play("CompletePuzzle");
    }

    public void Open2()
    {
        Animator anim2 = finalDoor.GetComponent<Animator>();
        audioData = finalDoor.GetComponent<AudioSource>();
        audioData.Play(0);
        anim2.SetTrigger("DoorOpen");
        FindObjectOfType<AudioManager>().Play("CompletePuzzle");
    }

    public void TurnOnTorches()
    {
        for(int i = 0; i < torches.gameObject.transform.childCount; i++)
        {
            var child = torches.gameObject.transform.GetChild(i);
            child.transform.GetChild(0).gameObject.SetActive(true);
            child.transform.GetChild(1).gameObject.SetActive(true);
        }
    }

    public void SetValue(string value)
    {
        placeInCode++;

        if(placeInCode <= codeLength)
        {
            attemptedCode += value;
        }

        if(placeInCode == codeLength)
        {
            CheckCode();

            groupAnim = this.GetComponent<Animator>();
            groupAnim.SetTrigger("GroupPressed");

            attemptedCode = "";
            placeInCode = 0;
        }
    }
}
