using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class TorchController : MonoBehaviour
{
    TorchLock torchLock;
    AudioSource audioData;

    public int reachRange = 100;


    void Update()
    {
        if (Input.GetKeyDown("e"))
        {
            Toggle();
        }
    }

    void Toggle()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit, reachRange))
        {
            torchLock = hit.transform.gameObject.GetComponentInParent<TorchLock>();

            if (torchLock != null)
            {
                if (hit.transform.GetChild(0).gameObject.activeSelf == true)
                {
                    hit.transform.GetChild(0).gameObject.SetActive(false);
                    hit.transform.GetChild(1).gameObject.SetActive(false);
                    FindObjectOfType<AudioManager>().Play("TorchOut");
                    torchLock.Subtract();
                }
                else
                {
                    hit.transform.GetChild(0).gameObject.SetActive(true);
                    hit.transform.GetChild(1).gameObject.SetActive(true);
                    FindObjectOfType<AudioManager>().Play("TorchOut");
                    torchLock.Add();
                }
            }
        }
    }
}
