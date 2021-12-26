using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class KeyController : MonoBehaviour
{

    public int reachRange = 100;
    public GameObject slotObject;
    [SerializeField] GameObject lightObj;

    public Slot slot;


    void Update()
    {
        if (Input.GetKeyDown("e"))
        {
            Hit();
        }
    }

    void Hit()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit, reachRange))
        {
            if(hit.transform.name == "SM_Rock_03")
            {
                Animator anim = hit.transform.GetComponent<Animator>();
                anim.SetTrigger("Move");
                FindObjectOfType<AudioManager>().Play("StoneSlide");
                FindObjectOfType<AudioManager>().Play("CompletePuzzle");
            }

            else if(hit.transform.tag == "DummyStone") {
                Animator anim = hit.transform.GetComponent<Animator>();
                anim.SetTrigger("Move");
                FindObjectOfType<AudioManager>().Play("StoneSlide");
            }

            if(hit.transform.name == "Key_B_02")
            {
                Debug.Log("Hit Key");
                slot = slotObject.GetComponent<Slot>();
                slot.PickUp();
                Destroy(hit.transform.gameObject);
            }

            if(hit.transform.name == "Chest" && slot.hasKey == true)
            {
                var anim = hit.transform.GetComponent<Animation>();
                anim.Play("ChestAnim");
                FindObjectOfType<AudioManager>().Play("CompletePuzzle");
                slot.Use();
                lightObj.SetActive(true);
                FindObjectOfType<GameManager>().EndGame();

            }
            else
            {
                Debug.Log("Nothing Happened");
            }
        }
    }
}
