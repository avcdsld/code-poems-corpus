public void enQueue(QueueElement newElement)
    {
        QueueElement pCur = pHead, pPre = null;

        while (pCur != null && pCur.weight < newElement.weight)
        {
            pPre = pCur;
            pCur = pCur.next;
        }

        newElement.next = pCur;

        if (pPre == null)
            pHead = newElement;
        else
            pPre.next = newElement;
    }