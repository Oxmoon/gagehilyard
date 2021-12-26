using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class SwitchController : MonoBehaviour
{
    private SwitchLock switchLock;
    private Animator[] anim;
    public int reachRange = 5;
    void Update()
    {
        if (Input.GetKeyDown("e"))
        {
            Move();
        }
    }

    void Move()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit, reachRange))
        {
            switchLock = hit.transform.gameObject.GetComponentInParent<SwitchLock>();

            if (switchLock != null && switchLock.canMove == true)
            {
                
                anim = hit.transform.GetComponentsInChildren<Animator>();
                Debug.Log("Name is: " +hit.transform.name);

                //Moves Down
                if(switchLock.GetPos(hit.transform.name) == 0)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim[0].SetTrigger("FirstHit");
                    switchLock.Move(hit.transform.name);
                }

                //Moves to the top
                else if (switchLock.GetPos(hit.transform.name) == 1)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim[0].SetTrigger("SecondHit");
                    switchLock.Move(hit.transform.name);
                }

                //Resets
                else if (switchLock.GetPos(hit.transform.name) == 2)
                {
                    FindObjectOfType<AudioManager>().Play("ButtonPress");
                    anim[0].SetTrigger("ThirdHit");
                    switchLock.Move(hit.transform.name);
                }
                else
                {
                    Debug.Log("Error in SC Move");
                }
            }
        }
    }
}
