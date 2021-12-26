using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class Slot : MonoBehaviour
{
    public Image keyImage;

    public bool hasKey;

    // Start is called before the first frame update
    private void Start()
    {
        keyImage.enabled = false;
    }

    public void PickUp()
    {
        keyImage.enabled = true;
        hasKey = true;
    }

    public void Use()
    {
        hasKey = false;
        keyImage.enabled = false;
    }
}
