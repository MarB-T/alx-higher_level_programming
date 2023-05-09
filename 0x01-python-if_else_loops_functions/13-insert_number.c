#include "lists.h"

/**
 * insert_node - inserts a node in an ordered list
 * @number: value of node to be added
 * @head: head of list in question
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if ((*head)->next == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	return (new);
}
