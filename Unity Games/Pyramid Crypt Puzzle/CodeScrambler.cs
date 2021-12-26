using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Random=UnityEngine.Random;
using TMPro;

//Scrambles the codes for the codeLock system and the cat statues
public class CodeScrambler : MonoBehaviour
{
    //Private GameObjects
    [SerializeField] GameObject WallCode, HiddenCode, PaperCode, cat1, cat2, cat3;

    public IDictionary<int, string> dict;
    string in_code = "albndemhk";
    public string scrambledCode;

    //NESW is RACN
    //default is "RACN";
    public string catSymbols;

    //New codes generated for CodeLock parts 1 and 2 and turn Lock
    public string code1, code2;
    public int turnCode;


    // Wall default code: albndemhk
    public void Awake()
    {
        //Generate random Codes for CodeLock and TurnLock with no repeats of three
        this.code1 = Convert.ToString(safeRandom(111, 999));
        this.code2 = Convert.ToString(safeRandom(111, 999));
        while(code1 == code2)
        {
            this.code2 = Convert.ToString(safeRandom(111,999));
        }

        //Random number 1 through 4 for the four cardinal directions.
        //South is 1, West is 2, North is 3, East is 4
        int temp = 111;
        while (hasRepeatOrZero(temp) == true)
        {
            temp = Random.Range(1,5)*100 + Random.Range(1,5)*10 + Random.Range(1,5);
        }
        this.turnCode = (temp);

        //Scramble wall symbols
        this.catSymbols = codeToDir(turnCode);
        this.scrambledCode = ScrambleString(in_code);
        this.dict = createCodeDict(scrambledCode);

        //Get TMPro
        TextMeshPro wallText = WallCode.GetComponent<TextMeshPro>();
        TextMeshPro paperText = PaperCode.GetComponent<TextMeshPro>();
        TextMeshPro hiddenText = HiddenCode.GetComponent<TextMeshPro>();
        TextMeshPro cat1Text = cat1.GetComponent<TextMeshPro>();
        TextMeshPro cat2Text = cat2.GetComponent<TextMeshPro>();
        TextMeshPro cat3Text = cat3.GetComponent<TextMeshPro>();

        //Set wall and ground symbols
        wallText.text = scrambledCode;
        hiddenText.text = dictToSym(this.dict, this.code1);
        paperText.text = dictToSym(this.dict, this.code2);
        cat1Text.text = catSymbols[0].ToString();
        cat2Text.text = catSymbols[1].ToString();
        cat3Text.text = catSymbols[2].ToString();
    }

    //The Number code needs to be converted to the chars "CNRA" which correspond with the
    //Font I am using for the symbols. 
    public string codeToDir(int in_code)
    {
        int hun = (in_code %1000)/100;
        int ten = (in_code %100)/10;
        int one = in_code %10;
        char[] result = new char[3];
        int[] a = {hun, ten, one};
        for (int i = 0; i < 3; i++)
        {
            switch(a[i]) 
            {
                case 1:
                    result[i] = 'C';
                    break;
                case 2:
                    result[i] = 'N';
                    break;
                case 3:
                    result[i] = 'R';
                    break;
                case 4:
                    result[i] = 'A';
                    break;
                default:
                    break;
            }
        }
        return new string(result);
    }

    //This method converts the given code to the corresponding symbols
    public string dictToSym(IDictionary<int, string> dict, string code)
    {
        int hun = (Convert.ToInt32(code) %1000)/100;
        int ten = (Convert.ToInt32(code) %100)/10;
        int one = Convert.ToInt32(code) %10;

        string code1 = dict[hun];
        string code2 = dict[ten];
        string code3 = dict[one];
        return ("" +code1 +code2 +code3);

    }

    //Scrambles a given string
    public string ScrambleString(string code) 
    { 
        char[] chars = new char[code.Length]; 
        int index = 0; 
        while (code.Length > 0) 
        {
            int next = Random.Range(0, code.Length);
            chars[index] = code[next];
            code = code.Substring(0, next) + code.Substring(next + 1);
            index++; 
        } 
        return new string(chars);
    }  

    //Dictionary to hold the int for the code lock and a ch for the TMPro object
    private IDictionary<int, string> createCodeDict(string scrambledCode)
    {
        int num = 1;
        IDictionary<int, string> dict = new Dictionary<int, string>();
        foreach (char ch in scrambledCode)
        {
            dict.Add(num,ch.ToString());
            num++;
        }
        return dict;
    }

    //Checks if digits match
    private bool hasRepeatOrZero(int in_number)
    {
        int hun = (in_number %1000)/100;
        int ten = (in_number %100)/10;
        int one = in_number %10;

        if (hun == ten || hun == one || ten == one)
        {
            return true;
        }
        else if(hun == 0 || ten == 0 || one == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    //Safely generate random number with given range
    private int safeRandom(int min, int max)
    {
        int num = Random.Range(min,max);
        while (hasRepeatOrZero(num) == true)
        {
            num = Random.Range(min,max);
        }
        return num;
    }
}