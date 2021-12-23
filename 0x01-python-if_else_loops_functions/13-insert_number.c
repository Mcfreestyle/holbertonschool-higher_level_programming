#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of the linked list
 * @number: number to insert
 *
 * Return: adress of the new node, NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp_node, *current_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	current_node = *head;

	if (!current_node || current_node->n > number)
	{
		new_node->next = current_node;
		current_node = new_node;
		return (new_node);
	}
	while (current_node)
	{
		if (current_node->n > number)
			break;
		tmp_node = current_node;
		current_node = current_node->next;
	}
	tmp_node->next = new_node;
	new_node->next = current_node;

	return (new_node);
}
