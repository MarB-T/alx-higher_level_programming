#include "lists.h"

/**
 * is_palindrome - function to check if linked list is palindrome
 * @head: pointer to linked list head
 * Return: 1 if palindrome 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	int count = 0, left = 0, right, *arr;
	int i = 0;
	listint_t *current;
	current = *head;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	arr = malloc(count * sizeof(int));
	if (arr == NULL)
	{
		return (0);
	}

	current = *head;
	while (current != NULL)
	{
		arr[i++] = current->n;
		current = current->next;
	}

	right = count - 1;
	while (left < right)
	{
		if (arr[left] != arr[right])
		{
			free(arr);
			return (0);
		}
		left++;
		right--;
	}

	free(arr);
	return (1);
}
