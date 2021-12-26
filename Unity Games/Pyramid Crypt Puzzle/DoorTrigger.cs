using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorTrigger : MonoBehaviour
{
    public GameObject door;
    public AudioSource doorAudio;

    private void OnTriggerEnter(Collider other)
    {
        Animator anim = door.GetComponent<Animator>();
        doorAudio.Play(0);
        anim.SetTrigger("DoorClose");
        Destroy(this.gameObject);
    }
}
