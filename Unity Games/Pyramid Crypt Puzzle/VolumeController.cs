using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Audio; 

public class VolumeController : MonoBehaviour
{
    public AudioMixer mixer;

    public void SetLevel(float SliderValue)
    {
        mixer.SetFloat("MasterVol", Mathf.Log10(SliderValue)*20);
    }
}
