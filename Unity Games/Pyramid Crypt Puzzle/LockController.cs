using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class LockController : MonoBehaviour
{
    CodeLock codeLock;
    Animator anim;

    public int reachRange = 100;
    private int count = 0;


    void Update()
    {
        if (Input.GetKeyDown("e"))
        {
            CheckHitObj();
        }
    }

    void CheckHitObj()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit, reachRange))
        {
            anim = hit.transform.GetComponent<Animator>();
            codeLock = hit.transform.gameObject.GetComponentInParent<CodeLock>();

            if (codeLock != null)
            {
                count++;
                if(count != 3) {
                    anim.SetTrigger("Pressed");
                }
                else {
                    count = 0;
                }
                FindObjectOfType<AudioManager>().Play("ButtonPress");
                string value = hit.transform.name;
                codeLock.SetValue(value);
            }
        }
    }
}