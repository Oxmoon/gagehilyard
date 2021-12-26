using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class TorchLock : MonoBehaviour
{
    int numLit = 7;
    public GameObject door;
    public GameObject paper;

    public void Add()
    {
        numLit++;
    }

    public void Subtract()
    {
        numLit--;
        if(numLit == 0)
        {
            Open();
            FindObjectOfType<AudioManager>().Play("CompletePuzzle");
        }
    }

    public void Open()
    {
        Animator anim = door.GetComponent<Animator>();
        FindObjectOfType<AudioManager>().Play("DoorMove");
        anim.SetTrigger("DoorOpen");
        paper.SetActive(true);
    }

}
