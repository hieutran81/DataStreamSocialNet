#include<stdio.h>
#include<stdlib.h>
#define M 10000
#define N 1000
#define THRES_HOLD 4
int m,n;
int link[M],adj[M];
float bwn[M];
int head[N],numPath[N],rank[N],visit[N];
float label[N];

void nhap(){
    FILE *f;
    int i,u,v;
    f = fopen("in.txt","r");
    fscanf(f,"%d",&n);
    fscanf(f,"%d",&m);
    for (i = 0; i <= n; i++) {
        head[i] = 0;
    }
    for (i = 1; i <= m; i++){
        fscanf(f,"%d",&u);
        fscanf(f,"%d",&v);
        link[i] = head[u];
        head[u] = i;
        link[i+m] = head[v];
        head[v] = i+m;
        adj[i] = v; adj[i+m] = u;
        bwn[i] = 0; bwn[i+m] = 0;
    }
    fclose(f);
}

void init(){
    for (int i = 0; i <= n; i++){
        visit[i] = 0;
        numPath[i] = 0;
        rank[i] = 0;
        label[i] = 0;
    }
}

void bfs(int s){
    int queue[N];
    int dau,cuoi,u,v,i,j;
    init();
    dau = 1; cuoi = 1; 
    queue[1] = s;
    visit[s] = 1;
    rank[s] = 0;
    numPath[s] = 1;
    while(dau <= cuoi){
        u = queue[dau]; dau++;
        i = head[u];
        while (i != 0){
            v = adj[i];
            if (visit[v] == 0){
                cuoi++;
                queue[cuoi] = v;
                visit[v] = 1;
                rank[v] = dau;
            }
            if (rank[v] > rank[u]){
                numPath[v] += numPath[u];
            }
            i = link[i];
        }
    }
    for (j = cuoi; j >=1 ; j--){
        u = queue[j];
        label[u] = 1;
        i = head[u];
        while (i != 0){
            v = adj[i];
            float added = (float) (label[v]/numPath[v]);
            if (rank[v] > rank[u]){
                label[u] += added;
                if (i <=m) bwn[i] += added; else bwn[i-m] += added;
            }
            i = link[i];
        }
    }
    for (int i = 1; i <= n; i++) printf("%d\t",queue[i]);
    printf("\n");
    for (int i = 1; i <= n; i++) printf("%f\t",label[i]);
    printf("\n");
    for (int i = 1; i <= n; i++) printf("%d\t",numPath[i]);
    printf("\n");
}

void xuli(){
    int i;
    
    for (i = 1; i <= n; i++ ){
        bfs(i);
    }
    for (i = 1; i <= m; i++) {
        bwn[i] = (float)(bwn[i]/2.0);
        printf("%d %d : %f\n",adj[i+m],adj[i],bwn[i]);
    }
}

void printFile(){
    FILE* f;
    f = fopen("out.txt","w");
    fprintf(f,"graph { ");
    for (int i = 1; i <= m; i++){
        if (bwn[i] < THRES_HOLD){
            fprintf(f,"%d -- %d ; ",adj[i+m],adj[i]);
        }
    }
    fprintf(f,"}");
    printf("hieuvodoi\n");
    fclose(f);

}

int main(){
    nhap();
    xuli();
    printFile();
    return 0;
}
