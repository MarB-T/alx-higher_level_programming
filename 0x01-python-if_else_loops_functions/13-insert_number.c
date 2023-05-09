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

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next != NULL)
	{
		if (current->n <= number && current->next->n >= number)
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
