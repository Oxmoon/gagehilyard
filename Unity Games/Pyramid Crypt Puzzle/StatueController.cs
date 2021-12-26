using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class StatueController : MonoBehaviour
{
    TurnLock turnLock;
    Animator anim;

    public int reachRange = 100;


    void Update()
    {
        if (Input.GetKeyDown("e"))
        {
            Turn();
        }
    }

    void Turn()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit, reachRange))
        {
            turnLock = hit.transform.gameObject.GetComponentInParent<TurnLock>();

            if (turnLock != null && turnLock.canTurn == true)
            {
                anim = hit.transform.GetComponent<Animator>();

                //turns west
                if(turnLock.GetPos(hit.transform.name) == 1)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim.SetTrigger("FirstHit");
                    turnLock.Turn(hit.transform.name);
                }

                //turns north
                else if (turnLock.GetPos(hit.transform.name) == 2)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim.SetTrigger("SecondHit");
                    turnLock.Turn(hit.transform.name);
                }

                //turns east
                else if (turnLock.GetPos(hit.transform.name) == 3)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim.SetTrigger("ThirdHit");
                    turnLock.Turn(hit.transform.name);
                }

                //turns south
                else if (turnLock.GetPos(hit.transform.name) == 4)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim.SetTrigger("FourthHit");
                    turnLock.Turn(hit.transform.name);
                }
                else
                {
                    Debug.Log("Error");
                }
            }
        }
    }
}
