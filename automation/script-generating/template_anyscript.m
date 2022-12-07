% suppose each subject's data is stored in its own directory
% for example obj1data1.txt-obj1data268.txt


addpath /your_path/.../some_package/;

% cd /your_path/.../your_working_dir


subjPath = "/your_path/.../subject_path";
subjFolders = struct2cell(dir(subjPath));
subjID = subjFolders(1, 5:end); % change to 5 when go to c2b2


tStart = tic; 
j = SUBNUM


tmp = subjID{1,j}; % get one subj ID
for k = 1:268 % loop thru 268 txt files
    textFilename=['/your_path/.../another_or_any_dir/' tmp '/ROI' num2str(k) '.txt'];
    fileID=fopen(textFilename, 'r');
    Data=fscanf(fileID,'%f');
    MyData(:,k)=Data;
    fclose(fileID);
end

ts = MyData'; %transpose to get timeseries data

[S{1,1},Q{1,1}] =dfcompute(ts,30,1,100,1,1);

subjQ_fileName = [tmp '_bestQ.mat'];
subjS_fileName = [tmp '_bestS.mat'];
bestQ_var = Q{1,1};
bestS_var = S{1,1};

save(subjQ_fileName, 'bestQ_var')
save(subjS_fileName, 'bestS_var')
clear MyData

tEnd = toc(tStart);

msg = "misson complete.";
totalTime = tEnd;
tmsg = ['Loop ' num2str(j) ' time: ',num2str(totalTime),' seconds (' tmp ')'];
disp(msg);
disp(tmsg)


