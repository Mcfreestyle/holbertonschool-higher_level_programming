#include "lists.h"

/**
 * checker - checks if a linked list is a palindrome
 * @head: pointer to head
 * @last: pointer to first node
 * @counter: counter
 * @num_comp: number of comparisons
 *
 * Return: 1 if the linked list is a palindrome, otherwise 0
 */
int checker(listint_t **head, listint_t *last, int counter, int num_comp)
{
	if (last == NULL)
		return (1);

	if (checker(head, last->next, counter - 1, num_comp))
	{
		if (counter <= num_comp)
		{
			if ((*head)->n == last->n)
			{
				*head = (*head)->next;
				return (1);
			}
		}
		else
			return (1);
	}
	return (0);
}

/**
 * is_palindrome - get the answer of other function
 *		to know if a linked list is palindrome
 * @head: pointer to head
 *
 * Return: 1 if the linked list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *head_tmp = *head;
	listint_t *nodo = *head;
	int c;

	for (c = 0; nodo; c++)
		nodo = nodo->next;

	if (*head == NULL)
		return (1);
	return (checker(&head_tmp, head_tmp, c, c / 2));
}
