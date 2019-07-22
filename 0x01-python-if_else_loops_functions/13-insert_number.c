#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - Inserts a node into a linked list
 *@head: Head of the list
 *@number: Value of the list
 *Return: Adress of the new node. Null if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *cpy, *aux;

	if (head == NULL || new_node == NULL)
		{
			free(new_node);
			return (NULL);
		}
	if (*head != NULL)
		{
			cpy = *head;
			aux = *head;
		}
	else
		{
			(*new_node).next = NULL;
			(*new_node).n = number;
			*head = new_node;
			return (new_node);
		}
	(*new_node).n = number;

	while (cpy != NULL)
		{
			if ((*cpy).n > number)
				break;
			aux = cpy;
			cpy = (*cpy).next;
		}

	if (cpy != NULL && aux == *head)
		{
			(*new_node).next = aux;
			*head = new_node;
			return (new_node);
		}

	(*new_node).next = (*aux).next;
	(*aux).next = new_node;

	return (new_node);
}
