### Script generating code

# Suppose you need to generate 100 matlab scripts,
# and they will be submitted to a Linux environment (like HPC) 
# for execution / computation
# each bash file will handle 1 matlab (.m) script


### Generate run files

auto_generating = function(total) {
  for (j in 1:total) {
    fileConn<-file(paste('submit_anyscript_',j,'.sh',sep=''))
    text = c('#!/bin/bash',
             paste('#$ -cwd -pe smp 4 -l mem=8G,time=4:: -S /bin/bash -N anyscript_',j,sep=''),
             paste('/nfs/apps/matlab/2018a/bin/matlab -nosplash -nojvm -nodesktop <nfcompute_anyscript_',j,'.m> result_anyscript_',j,'.log',sep='')
    )
    writeLines(text, fileConn)
    close(fileConn)
    
    ### Generate *.m file from template_anyscript.m file
    tx  <- readLines('template_anyscript.m')
    tx2  <- gsub(pattern = "SUBNUM", replace = j, x = tx)
    writeLines(tx2, con=paste('nfcompute_anyscript_',j,'.m',sep=''))
    
    message("finished scripts for seq: ", j)
  }
}

auto_generating(100)