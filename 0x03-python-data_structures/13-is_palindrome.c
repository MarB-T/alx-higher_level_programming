#include "lists.h"

/**
 * reverse_linked_list - reverses a linked list
 * @head: pointer to linked list
 * Return: revesed linked list
 */

listint_t *reversed_linked_list(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;
    
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
    
	return (prev);
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer to the list in question
 * Return: 1-is palindrome 0-is not palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head, *p1, *p2;
	listint_t *prev_slow = *head;
	listint_t *mid_node = NULL, *second_half;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			mid_node = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		second_half = reversed_linked_list(&second_half);

		p1 = *head;
		p2 = second_half;

		while (p1 != NULL && p2 != NULL)
		{
			if (p1->n != p2->n)
			{
				is_palindrome = 0;
				break;
			}
		p1 = p1->next;
		p2 = p2->next;
		}

		second_half = reversed_linked_list(&second_half);

		if (mid_node != NULL)
		{
			prev_slow->next = mid_node;
			mid_node->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}

	return (is_palindrome);
}
