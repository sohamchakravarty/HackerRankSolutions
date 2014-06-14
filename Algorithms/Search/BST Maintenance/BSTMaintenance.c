#include<stdio.h>
#include<stdlib.h>

struct node
{
    long key;
    int leftChilds,rightChilds;
    long leftDistance,rightDistance;
    
    struct node *left;
    struct node *right;
};

/*A function to calculate the distance*/
long distanceCalculator(int value)
{   
    static long distance = 0;
    distance += value;
    
    return distance;
}

/* Helper function that allocates a new node with the given key and
    NULL left and right pointers. */
struct node* newNode(int key)
{
    struct node* node = (struct node*)
                        malloc(sizeof(struct node));
    node->key   = key;
    node->leftChilds = node->rightChilds = 0;
    node->leftDistance = node->rightDistance = 0;
    node->left = node->right  = NULL;
    return(node);
}

int reverseHeight;
/*A function to insert node...1st call height=1*/
struct node* insert(struct node* node, int key,int height)
{
    if (node == NULL)
        return(newNode(key));
 
    distanceCalculator(height);
    if (key < node->key)
    {
       node->left  = insert(node->left, key, height+1); 
       node->leftChilds++;
       node->leftDistance += ++reverseHeight;
       distanceCalculator(node->rightDistance + (reverseHeight)*node->rightChilds);
    }
    else
    {
        node->right = insert(node->right, key,height+1);
        node->rightChilds++;
        node->rightDistance += ++reverseHeight;
        distanceCalculator(node->leftDistance + (reverseHeight)*node->leftChilds);
    }
         
    /* return the (unchanged) node pointer */
    return node;
}

int main()
{
  int n;  
  scanf("%d",&n);
    
  struct node *root = NULL;
  int i,arr[n];
  for(i=0;i<n;i++) {
      scanf("%d",&arr[i]);
      reverseHeight = 0;
      /* Constructing tree*/
      root = insert(root, arr[i],1); 
      printf("%lu\n",distanceCalculator(0));
  }

  return 0;
}