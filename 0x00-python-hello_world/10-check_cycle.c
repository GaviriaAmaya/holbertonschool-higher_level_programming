#include "lists.h"
/**
 *check_cycle - Proves if a list have a cycle
 *@list: List received
 *Return: If there's a cycle 1, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list;
	listint_t *j = list;

	if (list != NULL)
	{
		j = j->next;
		while (i != NULL && j != NULL && j->next != NULL)
		{
			if (i == j)
				return (1);
			i = i->next;
			j = j->next->next;
		}
	}
	return (0);
}
