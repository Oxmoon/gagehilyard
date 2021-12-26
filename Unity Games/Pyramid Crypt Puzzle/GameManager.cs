using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{

    CanvasGroup canvasGroup;
    public GameObject crosshair, canvas, text, slot;
    public bool creditsPlaying = false;
    public bool canLeave = false;
    Animator anim;
    public void EndGame()
    {
        canvasGroup = canvas.GetComponent<CanvasGroup>();
        FindObjectOfType<PlayerMovement>().canMove = false;
        crosshair.SetActive(false);
        slot.SetActive(false);
        Invoke("FadeIn", 4);
        creditsPlaying = true;
        anim = text.GetComponent<Animator>();
        StartCoroutine(returnToMenu());
    }

    //From Omnirift on YouTube
    //Used to fade in the credits UI
    public void FadeIn()
    {
        StartCoroutine(FadeCanvasGroup(canvasGroup, canvasGroup.alpha, 1));
    }
    private IEnumerator FadeCanvasGroup(CanvasGroup cg, float start, float end, float lerp = 0.5f)
    {
        float _timeStarted = Time.time;
        float timeSince = Time.time - _timeStarted;
        float percentageComplete = timeSince / lerp;

        while(true)
        {
            timeSince = Time.time - _timeStarted;
            percentageComplete = timeSince / lerp;
            
            float currentValue = Mathf.Lerp(start, end, percentageComplete);

            cg.alpha = currentValue;

            if (percentageComplete >= 1) break;
            yield return new WaitForEndOfFrame();
        }
    }

    private IEnumerator returnToMenu()
    {
        yield return new WaitForSeconds(4);
        anim.SetTrigger("Roll");
        yield return new WaitForSeconds(5);
        canLeave = true;
        yield return new WaitForSeconds(41);
        FindObjectOfType<PauseMenu>().PlayMainMenu();

    }
}
