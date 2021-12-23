#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to a node
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *low_step = list;
	listint_t *fast_step = list;

	if (!list)
		return (0);

	while (fast_step && fast_step->next)
	{
		fast_step = fast_step->next->next;
		low_step = low_step->next;
		if (fast_step == low_step)
			return (1);
	}
	return (0);
}
