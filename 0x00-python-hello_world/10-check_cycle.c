#include "lists.h"

/**
 * check_cycle - examines if a linked list has a cycle
 * @list: a linked list to check
 *
 * Return: If the list has circle return 1, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	
	if (!list)
		return (0);
	
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	
	return (0);
}
