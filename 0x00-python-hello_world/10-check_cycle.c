#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a loop in it
 * @list: head of the list to be checked
 * Return: 0-No cycle, 1-Cycle present
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
