using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PuzzleController : MonoBehaviour
{
    [SerializeField] GameObject codeS, codeL, turnL;
    CodeScrambler codeScrambler;
    CodeLock codeLock;
    TurnLock turnLock;

    IEnumerator Start()
    {
        yield return new WaitForSeconds(1);
        codeScrambler = codeS.GetComponent<CodeScrambler>();
        codeLock = codeL.GetComponent<CodeLock>();
        turnLock = turnL.GetComponent<TurnLock>();

        //Set Codes to the two puzzles
        codeLock.setCodes(codeScrambler.code1, codeScrambler.code2);
        turnLock.setCodes(codeScrambler.turnCode);
    }
}
